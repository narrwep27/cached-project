<template>
    <div class="page goal-comp">
        <h2>Goal Page</h2>
    </div>
</template>

<script>
import { VerifyToken } from '../services/CustomUser';

export default {
    name: 'Goal',
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