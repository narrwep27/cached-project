<template>
    <div class="page expense-list-comp">
        <ExpenseForm />
        <div class="expense-list-expense-div">
            <div class="expense-list-expense-div-header">
                <h3 class="expense-list-expense-div-header-date">Date</h3>
                <h3 class="expense-list-expense-div-header-tag">Tag</h3>
                <h3 class="expense-list-expense-div-header-cost">Cost</h3>
            </div>
            <Expense 
                :key="expense.id"
                v-for="expense in $store.state.expenses"
                :expense="expense"
            />
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
        sortedExpenses: []
    }),
    async beforeMount() {
        await this.checkToken();
        this.sortByDate();
    },
    beforeUpdate() {
        this.sortByDate();
    },
    methods: {
        sortByDate() {
            let expenses = this.$store.state.expenses;
            this.sortedExpenses = expenses.sort((a, b) => {
                let aDate = new Date(a.date);
                let bDate = new Date(b.date);
                return aDate - bDate;
            });
        },
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
        margin: 0 2em 0 0;
        flex-grow: 1;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        padding: 0 1em 1em 1em;
        height: fit-content;
        background-color: white;
    }
    .expense-form-comp {
        flex-shrink: 1;
    }

    .expense-list-expense-div-header {
        display: flex;
        gap: 8em;
        padding: 0 0 0 2.9em;
    }
    /* .expense-list-expense-div-header-date,
    .expense-list-expense-div-header-tag,
    .expense-list-expense-div-header-cost {} */
</style>