<template>
    <div class="page analysis-comp">
        <h2>Monthly Spending</h2>
        <h2>Expenses by Tag</h2>
            <form class="analysis-tag-chart-form" v-on:change="filterExpenseByDate">
                <label>Choose the Date:</label>
                <input type="month" placeholder="month" v-model="chartDate" />
                <button v-on:click.prevent="getTodaysDate">Back to Today</button>
            </form>
        <div class="analysis-column-pie-div">
            <column-chart 
                :data="tagExpenses" 
                class="analysis-column-chart"
                prefix="$"
                width="60%"
            />
            <br />
            <pie-chart 
                :data="tagExpenses" 
                class="analysis-pie-chart"
                legend="right"
                prefix="$"
                width="35%"
            />
        </div>
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser';

export default {
    name: 'Analysis',
    data: () => ({
        tagExpenses: [],
        chartDate: "",
        expensesByDate: [],
    }),
    async beforeMount() {
        await this.checkToken();
        this.getTagExpenses();
        this.getTodaysDate();
        this.filterExpenseByDate();
    },
    methods: {
        getTagExpenses() {
            let dataObj = {}
            this.$store.state.tags.forEach((tag) => {
                let totalCost = 0;
                this.$store.state.expenses.forEach((exp) => {
                    if (exp.tag === tag.id) {
                        totalCost = totalCost + parseInt(exp.cost);
                    }
                });
                dataObj[tag.name] = totalCost;
            });
            this.tagExpenses = dataObj;
        },
        getTodaysDate() {
            let today = new Date();
            let month = `${today.getMonth() + 1}`
            if (month.length === 1) { month = `0${month}`}
            this.chartDate = `${today.getFullYear()}-${month}`
        },
        filterExpenseByDate() {
            this.expensesByDate = this.$store.state.expenses.filter((exp) => {
                let dateString = exp.date.slice(0, 7)
                return dateString === this.chartDate
            })
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
    .analysis-tag-chart-form {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1em;
        width: fit-content;
        padding: 1em;
        margin: 0 3em;
    }
    .analysis-tag-chart-form > input[type="month"] {
        font-size: 18px;
        margin: .5em;
    }
    .analysis-tag-chart-form > button {
        height: 2.7em;
    }
    .analysis-column-pie-div {
        display: flex;
        justify-content: space-evenly;
        margin: 2em;
    }
    .analysis-column-chart {
        background-color: white;
        border: 1px solid #c0d7ee;
        border-radius: 5px;
        padding: 1em;
    }
</style>