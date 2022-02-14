<template>
    <div class="tag-comp">
        <div class="tag-item">
            <div class="tag-item-name-div">{{ tag.name }}</div>
            <div>
                <button 
                    class="tag-item-edit-show-btn"
                    v-on:click="showEditForm">
                    <PencilOutline :size="18" />
                </button>
            </div>
            <div>
                <button 
                    class="tag-item-delete-btn"
                    v-on:click="showDeleteWarning">
                    <DeleteEmptyOutline :size="18" />
                </button>
            </div>
        </div>
        <div :class="editFormDivClass">
            <form class="tag-comp-edit-form" v-on:submit.prevent="changeTag">
                <input type="text" placeholder="New tag name" v-model="newName"/>
                <button type="submit">Edit</button>
                <button v-on:click.prevent="showEditForm">Cancel</button>
            </form>
        </div>
        <div :class="deleteWarnDivClass">
            <AlertOutline class="alert-outline" :size="40" />
            <p>Warning: deleting this tag will also delete <b>all of the expenses</b> that belong to it.
                <br />Are you sure you want to delete it?
            </p>
            <button 
                class="tag-comp-delete-warn-div-delete-btn" 
                v-on:click="eraseTag">
                Delete
            </button>
            <button 
                class="tag-comp-delete-warn-div-cancel-btn" 
                v-on:click="showDeleteWarning">
                Cancel
            </button>
        </div>
    </div>
</template>

<script>
import PencilOutline from 'vue-material-design-icons/PencilOutline.vue';
import DeleteEmptyOutline from 'vue-material-design-icons/DeleteEmptyOutline.vue';
import AlertOutline from 'vue-material-design-icons/AlertOutline.vue';
import { EditTag, DeleteTag } from '../services/Tag';

export default {
    name: 'Tag',
    components: { 
        PencilOutline,
        DeleteEmptyOutline,
        AlertOutline
    },
    props: {
        tag: Object,
        index: Number
    },
    data: () => ({
        newName: '',
        editFormDivClass: "tag-comp-edit-form-div-hide",
        deleteWarnDivClass: "tag-comp-delete-warn-div-hide"
    }),
    methods: {
        showEditForm() {
            this.editFormDivClass === "tag-comp-edit-form-div-hide"
                ? this.editFormDivClass = "tag-comp-edit-form-div"
                : this.editFormDivClass = "tag-comp-edit-form-div-hide"
            this.deleteWarnDivClass === "tag-comp-delete-warn-div" 
                ? this.deleteWarnDivClass = "tag-comp-delete-warn-div-hide" : null
        },
        showDeleteWarning() {
            this.deleteWarnDivClass === "tag-comp-delete-warn-div-hide"
                ? this.deleteWarnDivClass = "tag-comp-delete-warn-div"
                : this.deleteWarnDivClass = "tag-comp-delete-warn-div-hide"
            this.editFormDivClass === "tag-comp-edit-form-div" 
                ? this.editFormDivClass = "tag-comp-edit-form-div-hide" : null
        },
        errorMissingField() {
            this.$snackbar.add({
                type: 'error',
                text: 'You must type in a new tag name to change the name of the chosen tag.'
            })
        },
        infoTagDelete() {
            this.$snackbar.add({
                type: 'info',
                text: `${this.tag.name} tag has been deleted.`
            })
        },
        async changeTag() {
            if (this.newName) {
                const res = await EditTag(this.tag.id, { name: this.newName });
                let tags = this.$store.state.tags;
                tags.splice(this.index, 1, res);
                this.$store.commit('setTags', tags);
                this.newName = '';
                this.editFormDivClass = 'tag-comp-edit-form-div-hide'
            } else {
                this.errorMissingField()
            }
        },
        async eraseTag() {
            await DeleteTag(this.tag.id);
            let tags = this.$store.state.tags;
            tags.splice(this.index, 1);
            this.$store.commit('setTags', tags);
            let expenses = this.$store.state.expenses;
            let newExp = expenses.filter(exp => exp.tag !== this.tag.id);
            this.$store.commit('setExpenses', newExp);
            this.infoTagDelete();
        }
    }
}
</script>

<style scoped>
    .tag-comp {
        border-top: 1px solid lightgray;
    }
    .tag-item {
        display: flex;
        justify-content: space-evenly;
        align-items: center;
        margin: .7em auto;
    }
    .tag-item-name-div {
        width: 65%;
    }
    .tag-item-edit-show-btn,
    .tag-item-delete-btn {
        border: 1px solid #2c3e50;
        border-radius: 3px;
    }

    .tag-comp-edit-form {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        padding: .7em;
        transition: 300ms
    }
    .tag-comp-edit-form-div-hide {
        display: none;
    }
    .tag-comp-edit-form button {
        font-size: 14px;
    }
    .tag-comp-delete-warn-div {
        display: grid;
        grid-template-columns: 1fr 3fr 3fr;
        grid-template-rows: 1fr 1fr;
        grid-template-areas: 
            "alertImage paragraph paragraph"
            "alertImage deleteBtn cancelBtn";
        align-items: center;
        justify-items: center;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        padding: 8px;
    }
    .tag-comp-delete-warn-div-hide {
        display: none;
    }
    .tag-comp-delete-warn-div .alert-outline {
        grid-area: alertImage;
    }
    .tag-comp-delete-warn-div p {
        grid-area: paragraph;
        margin: 0;
    }
    .tag-comp-delete-warn-div-delete-btn {
        grid-area: deleteBtn;
    }
    .tag-comp-delete-warn-div-cancel-btn {
        grid-area: cancelBtn;
    }
</style>