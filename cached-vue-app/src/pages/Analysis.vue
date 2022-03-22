<template>
    <div class="page analysis-comp">
        <h2>Monthly Spending</h2>
        <h2>Expenses by Tag</h2>
        <TagChart />
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser'
import TagChart from "../components/TagChart.vue"

export default {
    name: 'Analysis',
    components: {
        TagChart
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