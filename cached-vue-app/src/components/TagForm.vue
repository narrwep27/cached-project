<template>
    <div class="tag-form-comp">
        <h2>Create/Edit Tags</h2>
        <form v-on:submit.prevent="createNewTag" class="tag-form-form">
            <input type="text" placeholder="New tag name" v-model="newTagName" />
            <button type="submit" class="tag-form-form-btn">Create New Tag</button>
        </form>
        <Tag 
            :key="tag.id" 
            v-for="(tag, index) in $store.state.tags" 
            :tag="tag" 
            :index="index" 
        />
    </div>
</template>

<script>
import Tag from './Tag.vue';
import { CreateTag } from '../services/Tag';

export default {
    name: 'TagForm',
    components: { Tag },
    data: () => ({
        newTagName: ''
    }),
    methods: {
        async createNewTag() {
            if (this.newTagName){
                const res = await CreateTag({
                    user: this.$store.state.userId,
                    name: this.newTagName
                })
                this.$store.commit('setTags', [...this.$store.state.tags, res])
                this.newTagName = '';
            } else {
                this.errorMissingField();
            }
        },
        errorMissingField() {
            this.$snackbar.add({
                type: 'error',
                text: 'Please, type in a tag name to create a new tag.'
            })
        }
    }
}
</script>

<style scoped>
    .tag-form-comp {
        margin: 1.5em 0;
        border: 1px solid #2c3e50;
        border-radius: 8px;
        padding: 0 1em 1em 1em;
        background-color: white;
    }
    .tag-form-form {
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        padding: .5em;
        border: none;
    }
    .tag-form-form-btn {
        margin: 1em;
        font-size: 14px;
    }
</style>