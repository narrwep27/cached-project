<template>
    <div class="tagChart-comp">
        <form class="tagChart-chart-form" v-on:change="filterExpenseByDate">
            <label>Choose the Date:</label>
            <input type="month" placeholder="month" v-model="chartDate" />
            <button v-on:click.prevent="getMonthsExp">Back to Today</button>
        </form>
        <div class="tagChart-chart-div">
            <column-chart
                :data="tagExpenses"
                class="tagChart-column-chart"
                prefix="$"
                thousands=","
                width="60%"
                height="400px"
            />
            <pie-chart
                :data="tagExpenses"
                class="tagChart-pie-chart"
                legend="right"
                prefix="$"
                thousands=","
                width="35%"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "TagChart",
    data: () => ({
        tagExpenses: [],
        chartDate: "",
        expensesByDate: []
    }),
    beforeMount() {
        this.getMonthsExp()
    },
    methods: {
        getTagExpenses() {
            let dataObj = {}
            this.$store.state.tags.forEach((tag) => {
                let totalCost = 0
                this.expensesByDate.forEach((exp) => {
                    if (exp.tag === tag.id) {
                        totalCost += parseFloat(exp.cost)
                    }
                })
                dataObj[tag.name] = totalCost
            })
            this.tagExpenses = dataObj
        },
        filterExpenseByDate() {
            this.expensesByDate = this.$store.state.expenses.filter((exp) => {
                let dateString = exp.date.slice(0,7)
                return dateString === this.chartDate
            })
            this.getTagExpenses()
        },
        getMonthsExp() {
            let today = new Date()
            let month = `${today.getMonth() + 1}`
            if (month.length === 1) { month = `0${month}` }
            this.chartDate = `${today.getFullYear()}-${month}`
            this.filterExpenseByDate()
        }
    }
}
</script>

<style scoped>
    .tagChart-chart-form {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 1em;
        width: fit-content;
        padding: 1em;
        margin: 0 3em;
    }
    .tagChart-chart-form > input[type="month"] {
        font-size: 18px;
        margin: .5em;
    }
    .tagChart-chart-form > button {
        height: 2.7em;
    }
    .tagChart-chart-div {
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        margin: 2em;
        gap: 1em;
    }
    .tagChart-column-chart {
        background-color: white;
        border: 1px solid #c0d7ee;
        border-radius: 5px;
        padding: 1em;
    }
</style>