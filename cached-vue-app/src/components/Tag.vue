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
    </div>
</template>

<script>
import PencilOutline from 'vue-material-design-icons/PencilOutline.vue';
import DeleteEmptyOutline from 'vue-material-design-icons/DeleteEmptyOutline.vue';
import { EditTag } from '../services/Tag';

export default {
    name: 'Tag',
    components: { 
        PencilOutline,
        DeleteEmptyOutline
    },
    props: {
        tag: Object,
        index: Number
    },
    data: () => ({
        editFormDivClass: "tag-comp-edit-form-div-hide",
        newName: ''
    }),
    methods: {
        showEditForm() {
            this.editFormDivClass === "tag-comp-edit-form-div-hide"
                ? this.editFormDivClass = "tag-comp-edit-form-div"
                : this.editFormDivClass = "tag-comp-edit-form-div-hide"
        },
        showDeleteWarning() {},
        errorMissingField() {
            this.$snackbar.add({
                type: 'error',
                text: 'You must type in a new tag name to change the name of the chosen tag.'
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
        async deleteTag() {}
    }
}
</script>

<style scoped>
    .tag-comp {
        border-bottom: 1px solid lightgray;
        padding-bottom: .5em;
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
</style>