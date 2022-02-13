<template>
    <div class="expense-form-comp">
        <form class="expense-form-form" v-on:submit.prevent="createExpense">
            <h2>Record an Expense:</h2>
            <label>Date of expense:</label>
            <input type="date" />
            <label>Choose a tag:</label>
            <select class="tag-div-select">
                <option value="">--Select a tag--</option>
                <option 
                    :key="tag" 
                    v-for="tag in $store.state.tags"
                    :value="tag.id">
                    {{ tag.name }}
                </option>
            </select>
            <label>Cost:</label>
            <input type="number" step=0.01 min="0" placeholder="Cost" />
            <button class="expense-form-btn" type="submit">Create Expense</button>
        </form>
        <TagForm />
    </div>
</template>

<script>
import TagForm from './TagForm.vue';

export default {
    name: 'ExpenseForm',
    components: { TagForm },
    data: () => ({
        createTagDisplay: false
    }),
    methods: {
        async createExpense() {},
        showCreateTagForm() {
            this.createTagDisplay === false ? this.createTagDisplay = true : this.createTagDisplay = false
        }
    }
}
</script>

<style scoped>
    .expense-form-comp {
        margin: 0 3em;
        width: 35%;
    }
    .expense-form-form {
        padding-top: 0;
    }
    .expense-form-form label {
        margin-top: 1em;
    }
    .expense-form-btn {
        margin: 1.5em auto;
        margin-bottom: .5em;
        width: 50%;
    }

    .tag-div-comp {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
        margin: 1.5em 0;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        width: 100%;
        height: 20%;
    }
    .tag-div-select {
        height: 2.5em;
        margin: 1em;
    }
    .tag-div-create-btn {
        margin: 1em;
        font-size: 14px;
    }
</style>