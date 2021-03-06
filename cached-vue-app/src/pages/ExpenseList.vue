<template>
    <div class="page expense-list-comp">
        <ExpenseForm />
        <div class="expense-list-form-expense-container">
            <form 
                class="expense-list-expense-div-filter-form"
                v-on:change.prevent="filterExpenses">
                <p>Filter expenses:</p>
                <select v-model="filterYearChoice">
                    <option :value="null">--Select Year--</option>
                    <option 
                        :key="year" 
                        v-for="year in filterYearOptions" 
                        :value="year">
                        {{ year }}
                    </option>
                </select>
                <select v-model="filterMonthChoice" :disabled="!filterYearChoice">
                    <option :value="null">--Select Month--</option>
                    <option 
                        :key="month.num" 
                        v-for="month in filterMonthOptions" 
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
                <button v-on:click.prevent="clearFilters">Clear filters</button>
            </form>
            <div class="expense-list-expense-div">
                <div class="expense-list-expense-div-header">
                    <h3 class="expense-list-expense-div-header-date">Date</h3>
                    <h3 class="expense-list-expense-div-header-tag">Tag</h3>
                    <h3 class="expense-list-expense-div-header-cost">Cost</h3>
                </div>
                <div v-if="filterYearChoice || filterTagChoice">
                    <div v-if="filteredExpenses.length > 0">
                        <Expense 
                            :key="expense.id"
                            v-for="expense in filteredExpenses"
                            :expense="expense"
                            v-on:filterExpenses="filterExpenses"
                        />
                    </div>
                    <div v-else>No expenses fit those filters</div>
                </div>
                <div v-else>
                    <Expense 
                        :key="expense.id"
                        v-for="expense in $store.state.expenses"
                        :expense="expense"
                    />
                </div>
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
        filterYearOptions: [],
        filterMonthOptions: [],
        filterYearChoice: null,
        filterMonthChoice: null,
        filterTagChoice: null,
        filteredExpenses: []
    }),
    async beforeMount() {
        await this.checkToken();
        this.getFilterYearOptions();
        this.getFilterMonthOptions();
    },
    beforeUpdate() {
        this.sortedExpenses = this.$store.getters.sortExpensesByDate;
        this.getFilterYearOptions();
        this.getFilterMonthOptions();
    },
    methods: {
        getFilterYearOptions() {
            let years = this.$store.state.expenses.map((exp) => {
                return exp.date.slice(0, 4);
            });
            this.filterYearOptions = [...new Set(years)];
        },
        getFilterMonthOptions() {
            let months = this.$store.state.expenses.map((exp) => {
                return exp.date.slice(5, 7);
            });
            let monthSet = [...new Set(months)];
            let sortedMonths = monthSet.map(month => parseInt(month)).sort((a, b) => { return a - b })
            this.filterMonthOptions = sortedMonths.map((month) => {
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
        filterExpenses() {
            if (this.filterYearChoice || this.filterTagChoice) {
                if (this.filterYearChoice && !this.filterTagChoice) {
                    this.filteredExpenses = this.$store.state.expenses.filter((exp) => {
                        return exp.date.slice(0, 4) === this.filterYearChoice;
                    });
                    if (this.filterMonthChoice) {
                        this.filteredExpenses = this.filteredExpenses.filter((exp) => {
                            return parseInt(exp.date.slice(5, 7)) === this.filterMonthChoice;
                        })
                    }
                } else if (this.filterTagChoice && !this.filterYearChoice) {
                    this.filteredExpenses = this.$store.state.expenses.filter((exp) => {
                        return exp.tag === this.filterTagChoice;
                    });
                } else if (this.filterYearChoice && this.filterTagChoice) {
                    this.filteredExpenses = this.$store.state.expenses.filter((exp) => {
                        return exp.date.slice(0, 4) === this.filterYearChoice;
                        }).filter((exp) => {
                            return exp.tag === this.filterTagChoice;
                        });
                    if (this.filterMonthChoice) {
                        this.filteredExpenses = this.filteredExpenses.filter((exp) => {
                            return parseInt(exp.date.slice(5, 7)) === this.filterMonthChoice;
                        });
                    }
                }
            } else { 
                this.filteredExpenses = [];
                this.filterMonthChoice = null;
            }
        },
        clearFilters() {
            this.filterYearChoice = null;
            this.filterMonthChoice = null;
            this.filterTagChoice = null;
            this.filteredExpenses = [];
        },
        async checkToken() {
            if (localStorage.getItem('accessToken')) {
                const res = await VerifyToken(localStorage.getItem('accessToken'));
                if (res.status === 401) {
                    this.$store.commit('clearUser');
                    this.$router.push('/');
                    this.warningExpire();
                }
            } else {
                this.$store.commit('clearUser');
                this.$router.push('/');
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
    .expense-list-expense-div-filter-form select:disabled {
        cursor: not-allowed;
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