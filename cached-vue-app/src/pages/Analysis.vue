<template>
    <div class="page analysis-comp">
        <h2>Expense Analysis</h2>
        <column-chart 
            :data="tagExpenses" 
            class="column-chart"
            prefix="$"
            width="60%"
        />
        <br />
        <pie-chart 
            :data="tagExpenses" 
            class="pie-chart"
            legend="right"
            prefix="$"
            width="35%"
        />
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser';

export default {
    name: 'Analysis',
    data: () => ({
        tagExpenses: []
    }),
    async beforeMount() {
        await this.checkToken();
        this.getTagExpenses();
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
    .column-chart {
        margin: 1em auto;
        background-color: white;
        border: 1px solid #c0d7ee;
        border-radius: 5px;
    }
    .pie-chart {
        margin: 1em auto;
    }
</style>