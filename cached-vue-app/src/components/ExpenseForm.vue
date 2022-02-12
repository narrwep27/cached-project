<template>
    <div class="expense-form-comp">
        <h2>Record an Expense:</h2>
        <form class="expense-form-form" v-on:submit.prevent="createExpense">
            <label>Date of expense:</label>
            <input type="date" />
            <div class="tag-div-comp">
                <select class="tag-div-select">
                    <option value="">--Select a tag--</option>
                </select>
                <h3>OR</h3>
                <button 
                    class="tag-div-create-btn" 
                    v-on:click.prevent="showCreateTagForm">
                    Create New Tag
                </button>
                <div class="tag-div-create-div" v-if="createTagDisplay">
                    <form class="tag-div-create-form" v-on:submit.prevent="showCreateTagForm">
                        <label>New tag:</label>
                        <input type="text" placeholder="New tag name" />
                        <button type="submit">Create Tag</button>
                    </form>
                </div>
            </div>
            <label>Cost:</label>
            <input type="number" step=0.01 min="0" placeholder="Cost" />
            <button class="expense-form-btn" type="submit">Create Expense</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'ExpenseForm',
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
        margin: 0 5em;
        width: 28%;
    }
    .expense-form-form {
        padding-top: 2.5em;
        height: 335px;
    }
    .expense-form-btn {
        margin: 1.5em auto;
        width: 50%;
        transition: 100ms
    }
    .expense-form-btn:active {
        font-size: 15px;
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
        transition: 100ms;
        font-size: 14px;
    }
    .tag-div-create-btn:active {
        font-size: 15px;
        margin: 19px;
    }

    .tag-div-create-div {
        position: absolute;
        height: 399px;
        width: 28%;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        top: 140px;
        margin-left: -2px;
        background-color: rgb(0,0,0,.2);
    }
    .tag-div-create-form {
        display: flex;
        width: 70%;
        height: 30%;
        border: 1px solid #2c3e50;
        margin: 5em auto;
        padding: 1em 1em;
    }
    .tag-div-create-form button {
        margin: .8em;
        font-size: 14px;
    }
    .tag-div-create-form button:active {
        font-size: 13px;
    }
</style>