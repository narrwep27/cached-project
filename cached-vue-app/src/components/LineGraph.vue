<template>
    <div class='lineGraph-comp'>
        <select class="lineGraph-date-select" title="lineGraph-date-select" v-model="rangeLength" v-on:change="getDateRange">
            <option value="6">Past 6 Months</option>
            <option value="9">Past 9 Months</option>
            <option value="12">Past 1 year</option>
        </select>
        <line-chart 
            :data="monthlyTotals" 
            class="lineGraph-graph"
            width="90%"
            :curve="false"
            prefix="$"
            thousands=","
        />
    </div>
</template>

<script>
export default {
    name: 'LineGraph',
    data: () => ({
        startDate: {},
        endDate: {},
        monthlyTotals: {},
        rangeLength: "6"
    }),
    beforeMount() {
        this.getDateRange()
    },
    methods: {
        getDateRange() {
            const end = new Date()
            this.endDate = {
                month: end.getMonth() + 1,
                year: end.getFullYear()
            }
            const start = new Date(this.endDate.year, this.endDate.month - parseInt(this.rangeLength))
            this.startDate = {
                month: start.getMonth() + 1,
                year: start.getFullYear()
            }
            this.getMonthlyTotals()
        },
        getMonthlyTotals() {
            this.monthlyTotals = {}
            for (let i = this.startDate.year; i <= this.endDate.year; i++) {
                let endMonth = i === this.endDate.year ? this.endDate.month : 12
                let startMonth = i === this.startDate.year ? this.startDate.month: 1
                for (let j = startMonth; j <= endMonth; j++) {
                    let monthStr = j < 10 ? `0${j}` : `${j}`
                    let allMonthCosts = this.$store.state.expenses.filter((exp) => {
                        return exp.date.slice(0,7) === `${i}-${monthStr}`
                    }).map(filteredExp => parseFloat(filteredExp.cost))
                    let monthName;
                    switch (j) {
                        case 1:
                            monthName = "Jan"
                            break
                        case 2:
                            monthName = "Feb"
                            break
                        case 3:
                            monthName = "Mar"
                            break
                        case 4:
                            monthName = "Apr"
                            break
                        case 5:
                            monthName = "May"
                            break
                        case 6:
                            monthName = "Jun"
                            break
                        case 7:
                            monthName = "Jul"
                            break
                        case 8:
                            monthName = "Aug"
                            break
                        case 9:
                            monthName = "Sep"
                            break
                        case 10:
                            monthName = "Oct"
                            break
                        case 11:
                            monthName = "Nov"
                            break
                        case 12:
                            monthName = "Dec"
                            break
                        default:
                            monthName = null
                    }
                    this.monthlyTotals[`${monthName} ${i}`] = 
                        allMonthCosts.reduce((acc, val) => {
                            return acc += val
                        }, 0)
                }
            }
        },
    }
}
</script>

<style scoped>
    .lineGraph-comp {
        display: flex;
        flex-direction: column;
        gap: 1em;
        align-items: center;
    }
    .lineGraph-date-select {
        align-self: start;
        margin: 0 10%;
    }
    .lineGraph-graph {
        justify-self: center;
    }
</style>