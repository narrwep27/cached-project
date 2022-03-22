<template>
    <div class='lineGraph-comp'>
    </div>
</template>

<script>
export default {
    name: 'LineGraph',
    data: () => ({
        startDate: {},
        endDate: {},
        monthlyTotals: {}
    }),
    beforeMount() {
        this.getInitialDates()
        this.getMonthlyTotals()
    },
    methods: {
        getInitialDates() {
            const end = new Date()
            this.endDate = {
                month: end.getMonth(),
                year: end.getFullYear()
            }
            const start = new Date(this.endDate.year, this.endDate.month - 5)
            this.startDate = {
                month: start.getMonth(),
                year: start.getFullYear()
            }
        },
        getMonthlyTotals() {
            for (let i = this.startDate.year; i <= this.endDate.year; i++) {
                let endMonth = i === this.endDate.year ? this.endDate.month : 11
                let startMonth = i === this.startDate.year ? this.startDate.month: 0
                for (let j = startMonth; j <= endMonth; j++) {
                    let monthStr;
                    switch (j) {
                        case 0:
                            monthStr = "Jan"
                            break
                        case 1:
                            monthStr = "Feb"
                            break
                        case 2:
                            monthStr = "Mar"
                            break
                        case 3:
                            monthStr = "Apr"
                            break
                        case 4:
                            monthStr = "May"
                            break
                        case 5:
                            monthStr = "Jun"
                            break
                        case 6:
                            monthStr = "Jul"
                            break
                        case 7:
                            monthStr = "Aug"
                            break
                        case 8:
                            monthStr = "Sep"
                            break
                        case 9:
                            monthStr = "Oct"
                            break
                        case 10:
                            monthStr = "Nov"
                            break
                        case 11:
                            monthStr = "Dec"
                            break
                        default:
                            monthStr = null
                    }
                    this.monthlyTotals[`${monthStr} ${i}`] = 0
                }
            }
        }
    }
}
</script>

<style scoped>
    .lineGraph-comp {
        display: flex;
    }
</style>