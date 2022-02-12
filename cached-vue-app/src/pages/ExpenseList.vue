<template>
    <div class="page expense-list-comp">
        <ExpenseForm />
        <div class="expense-list-expense-div">
            <Expense />
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
        expenses: []
    }),
    async beforeMount() {
        await this.checkToken()
    },
    methods: {
        async checkToken() {
            if (localStorage.getItem('accessToken')) {
                const res = await VerifyToken(localStorage.getItem('accessToken'));
                if (res.status === 401) {
                    this.$store.commit('clearUser');
                    this.$router.push('/home');
                    this.warningExpire();
                }
            } else {
                this.$store.commit('clearUser');
                this.$router.push('/home');
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
    .expense-list-expense-div {
        margin: 0 1em
    }
</style>