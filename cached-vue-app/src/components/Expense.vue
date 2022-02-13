<template>
    <div class="expense-comp">
        <div class="expense-item">
            <div class="expense-item-date">
                <p>{{ dateString }}</p>
            </div>
            <div class="expense-item-tag">
                <p>{{ tagObj.name }}</p>
            </div>
            <div class="expense-item-cost">
                <p>{{ costStr }}</p>
            </div>
            <div class="expense-item-showEdit-btn">
                <button v-on:click="toggleEditDiv"><PencilOutline /></button>
            </div>
            <div class="expense-item-delete-btn">
                <button v-on:click="eraseExpense"><DeleteEmptyOutline /></button>
            </div>
        </div>
        <div :class="editDivClass">
            <form class="expense-item-edit-div-form" v-on:submit.prevent="changeExpense">
                <input type="date" v-model="expenseEdit.date"/>
                <select v-model="expenseEdit.tag">
                    <option value="">--Select a tag--</option>
                    <option 
                        :key="tag.id" 
                        v-for="tag in $store.state.tags"
                        :value="tag.id">
                        {{ tag.name }}
                    </option>
                </select>
                <input 
                    type="number" step="0.01" min="0" 
                    v-model="expenseEdit.cost" 
                    :placeholder="expense.cost"
                />
                <button type="submit">Edit</button>
                <button v-on:click.prevent="toggleEditDiv">Cancel</button>
            </form>
        </div>
    </div>
</template>

<script>
import PencilOutline from 'vue-material-design-icons/PencilOutline.vue';
import DeleteEmptyOutline from 'vue-material-design-icons/DeleteEmptyOutline.vue';
import { EditExpense, DeleteExpense } from '../services/Expense';

export default {
    name: 'Expense',
    components: {
        PencilOutline,
        DeleteEmptyOutline
    },
    props: {
        expense: Object,
        index: Number
    },
    data: () => ({
        dateString: '',
        tagObj: '',
        costStr: '',
        editDivClass: 'expense-item-edit-div-hide',
        expenseEdit: {
            date: null,
            tag: '',
            cost: null
        }
    }),
    beforeMount() {
        this.dateConvert();
        this.getTagName();
        this.costToStr();
    },
    beforeUpdate() {
        this.dateConvert();
        this.getTagName();
        this.costToStr();
    },
    methods: {
        dateConvert() {
            let year = parseInt(this.expense.date.slice(0,5));
            let month = parseInt(this.expense.date.slice(5, 7));
            let day = parseInt(this.expense.date.slice(8, 10));
            let date = new Date(year, month - 1, day);
            let strDate = date.toString();
            this.dateString = strDate.slice(4, 10) + ', ' + strDate.slice(11, 15);
        },
        getTagName() {
            let userTags = this.$store.state.tags;
            this.tagObj = userTags.find(arrItem => arrItem.id === this.expense.tag);
        },
        costToStr() {
            this.costStr = `$${this.expense.cost}`;
        },
        toggleEditDiv() {
            this.editDivClass === 'expense-item-edit-div-hide'
                ? this.editDivClass = 'expense-item-edit-div'
                : this.editDivClass = 'expense-item-edit-div-hide'
        },
        infoDeleteConfirm() {
            this.$snackbar.add({
                type: 'info',
                text: 'Expense has been deleted.'
            })
        },
        async changeExpense() {
            let res = await EditExpense(this.expense.id, {
                cost: this.expenseEdit.cost || this.expense.cost,
                date: this.expenseEdit.date || this.expense.date,
                tag: this.expenseEdit.tag || this.expense.tag,
                user: this.$store.state.userId
            })
            let expensesArr = this.$store.state.expenses;
            let newExpArr = expensesArr.filter(exp => exp.id !== this.expense.id);
            newExpArr = [...newExpArr, res];
            this.$store.commit('setExpenses', newExpArr);
            this.expenseEdit.date = null;
            this.expenseEdit.tag = '';
            this.expenseEdit.cost = null;
            this.editDivClass = "expense-item-edit-div-hide";
        },
        async eraseExpense() {
            await DeleteExpense(this.expense.id);
            let newExpenses = this.$store.state.expenses.filter(exp => exp.id !== this.expense.id);
            this.$store.commit('setExpenses', newExpenses);
            this.infoDeleteConfirm();
        }
    }
}
</script>

<style scoped>
    .expense-item {
        display: flex;
        gap: 1em;
        border-top: 1px solid lightgray;
        align-items: center;
    }
    .expense-item-date,
    .expense-item-tag,
    .expense-item-cost {
        width: 9em;
    }
    .expense-item-showEdit-btn button,
    .expense-item-delete-btn button {
        border: 1px solid #2c3e50;
        border-radius: 3px;
        margin: 5px 8px;
    }
    .expense-item-edit-div {}
    .expense-item-edit-div-hide {
        display: none;
    }
    .expense-item-edit-div-form {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding: 10px 10px 5px 10px;
        margin: 10px;
    }
    .expense-item-edit-div select {
        height: 2.5em;
    }
    .expense-item-edit-div button {
        font-size: 14px;
        height: 35px;
    }
</style>