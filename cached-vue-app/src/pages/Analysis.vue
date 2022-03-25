<template>
    <div class="page analysis-comp">
        <div class="analysis-lineGraph-div">
            <h2>Total Spent each Month</h2>
            <LineGraph />
        </div>
        <div class="analysis-tagChart-div">
            <h2>Total Spent by Tag</h2>
            <TagChart />
        </div>
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser'
import TagChart from "../components/TagChart.vue"
import LineGraph from "../components/LineGraph.vue"

export default {
    name: 'Analysis',
    components: {
        TagChart,
        LineGraph
    },
    data: () => ({}),
    async beforeMount() {
        await this.checkToken();
    },
    methods: {
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
    .analysis-lineGraph-div {
        margin: 2em 8%;
    }
    .analysis-tagChart-div {
        margin: 2em;
    }
</style>