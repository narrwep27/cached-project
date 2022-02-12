<template>
    <div class="tag-form-comp">
        <select class="tag-form-select">
            <option value="">--Select a tag--</option>
        </select>
        <h3>OR</h3>
        <button 
            class="tag-form-createTag-btn" 
            v-on:click.prevent="showCreateTagForm">
            CreateNewTag
        </button>
        <form class="tag-form-createTag-form" v-if="createDisplay">
            <label>New tag:</label>
            <input type="text" placeholder="New tag name" />
            <button type="submit">Create Tag</button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'TagForm',
    data: () => ({
        createDisplay: false
    }),
    methods: {
        showCreateTagForm() {
            this.createDisplay === false ? this.createDisplay = true : this.createDisplay = false
        }
    }
}
</script>

<style scoped>
    .tag-form-comp {
        display: flex;
        flex-direction: row;
        align-items: center;
        margin: 1.5em 0;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        width: 100%;
        height: 20%;
    }
    .tag-form-select {
        height: 2.5em;
        margin: 1em;
    }
    .tag-form-createTag-btn {
        margin: 1em;
        transition: 100ms;
    }
    .tag-form-createTag-btn:active {
        font-size: 15px;
    }
    .tag-form-createTag-form {
        display: flex;
        border: none;
        margin: 1em;
        padding: 0;
    }
    .tag-form-creatTag-form button {
        margin: .8em;
        font-size: 14px;
    }
    .tag-form-createTag-form button:active {
        font-size: 12px;
    }
</style>