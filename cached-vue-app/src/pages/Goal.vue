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
        await this.checkToken()
    },
    methods: {
        async checkToken() {
            if (localStorage.getItem('accessToken')) {
                const res = await VerifyToken(localStorage.getItem('accessToken'));
                if (res.status === 401) {
                    this.$router.push('/home');
                }
            } else {
                this.$router.push('/home')
            }
        }
    }
}
</script>