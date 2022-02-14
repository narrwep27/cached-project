<template>
    <div class="page expense-list-comp">
        <ExpenseForm />
        <div class="expense-list-form-expense-container">
            <form 
                class="expense-list-expense-div-filter-form"
                v-on:click.prevent="filterExpenses">
                <p>Filter expenses:</p>
                <select v-model="filterYearChoice">
                    <option :value="null">--Select Year--</option>
                    <option 
                        :key="year" 
                        v-for="year in filterYears" 
                        :value="year">
                        {{ year }}
                    </option>
                </select>
                <select v-model="filterMonthChoice">
                    <option :value="null">--Select Month--</option>
                    <option 
                        :key="month.num" 
                        v-for="month in filterMonths" 
                        :value="month.num">
                        {{ month.name }}
                    </option>
                </select>
                <select v-model="filterTagChoice">
                    <option :value="null">--Select Tag--</option>
                    <option 
                        :key="tag.id" 
                        v-for="tag in $store.state.tags"
                        :value="tag.id">
                        {{ tag.name }}
                    </option>
                </select>
                <button type="submit">Filter</button>
                <button v-on:click.prevent="clearFilters">Clear filters</button>
            </form>
            <div class="expense-list-expense-div">
                <div class="expense-list-expense-div-header">
                    <h3 class="expense-list-expense-div-header-date">Date</h3>
                    <h3 class="expense-list-expense-div-header-tag">Tag</h3>
                    <h3 class="expense-list-expense-div-header-cost">Cost</h3>
                </div>
                <Expense 
                    :key="expense.id"
                    v-for="expense in $store.state.expenses"
                    :expense="expense"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser';
import ExpenseForm from '../components/ExpenseForm.vue';
import Expense from '../components/Expense.vue';

export default {
    name: 'ExpenseList',
    components: {
        ExpenseForm,
        Expense
    },
    data: () => ({
        sortedExpenses: [],
        filterYears: [],
        filterMonths: [],
        filterTags: [],
        filterYearChoice: null,
        filterMonthChoice: null,
        filterTagChoice: null,
    }),
    async beforeMount() {
        await this.checkToken();
        this.sortByDate();
        this.getFilterYears();
        this.getFilterMonths();
    },
    beforeUpdate() {
        this.sortByDate();
        this.getFilterYears();
        this.getFilterMonths();
    },
    methods: {
        sortByDate() {
            let expenses = this.$store.state.expenses;
            this.sortedExpenses = expenses.sort((a, b) => {
                let aDate = new Date(a.date);
                let bDate = new Date(b.date);
                return bDate - aDate;
            });
        },
        getFilterYears() {
            let years = this.$store.state.expenses.map((exp) => {
                return exp.date.slice(0, 4);
            });
            this.filterYears = [...new Set(years)];
        },
        getFilterMonths() {
            let months = this.$store.state.expenses.map((exp) => {
                return exp.date.slice(5, 7);
            });
            let monthSet = [...new Set(months)];
            let sortedMonths = monthSet.map(month => parseInt(month)).sort((a, b) => { return a - b })
            this.filterMonths = sortedMonths.map((month) => {
                if (month === 1) { return { name: 'January', num: 1 } }
                else if (month === 2) { return { name: 'February', num: 2 } }
                else if (month === 3) {return { name: 'March', num: 3 } }
                else if (month === 4) { return { name: 'April', num: 4} }
                else if (month === 5) { return { name: 'May', num: 5 } }
                else if (month === 6) { return { name: 'June', num: 6 } }
                else if (month === 7) { return { name: 'July', num: 7 } }
                else if (month === 8) { return { name: 'August', num: 8 } }
                else if (month === 9) { return { name: 'September', num: 9 } }
                else if (month === 10) { return { name: 'October', num: 10 } }
                else if (month === 11) { return { name: 'November', num: 11 } }
                else if (month === 12) { return { name: 'December', num: 12 } }
            })
        },
        filterExpenses() {},
        clearFilters() {
            this.filterYearChoice = null;
            this.filterMonthChoice = null;
            this.filterTagChoice = null;
        },
        async checkToken() {
            if (localStorage.getItem('accessToken')) {
                const res = await VerifyToken(localStorage.getItem('accessToken'));
                if (res.status === 401) {
                    this.$store.commit('clearUser');
                    this.$router.push('/home');
                    this.warningExpire();
                }
            } else {
                this.$store.commit('clearUser');
                this.$router.push('/home');
            }
        },
        warningExpire() {
            this.$snackbar.add({
                type: 'warning',
                text: 'Your session has expired. Please, log in again to access your account.'
            })
        }
    }
}
</script>

<style scoped>
    .expense-list-comp {
        display: flex;
        padding-top: 1em;
    }
    .expense-list-form-expense-container {
        flex-grow: 2;
        margin-right: 5em;
    }
    .expense-list-expense-div {
        margin: 1em 0;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        padding: 0 1em 1em 1em;
        height: fit-content;
        background-color: white;
    }
    .expense-form-comp {
        flex-grow: 1;
    }
    .expense-list-expense-div-filter-form {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        padding: .7em;
        align-items: center;
    }
    .expense-list-expense-div-filter-form select {
        height: 2.5em;
    }

    .expense-list-expense-div-header {
        display: flex;
        gap: 8em;
        padding: 0 0 0 2.9em;
    }
    /* .expense-list-expense-div-header-date,
    .expense-list-expense-div-header-tag,
    .expense-list-expense-div-header-cost {} */
</style>