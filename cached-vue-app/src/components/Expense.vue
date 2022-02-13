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
                <button><DeleteEmptyOutline /></button>
            </div>
        </div>
        <div :class="editDivClass"></div>
    </div>
</template>

<script>
import PencilOutline from 'vue-material-design-icons/PencilOutline.vue';
import DeleteEmptyOutline from 'vue-material-design-icons/DeleteEmptyOutline.vue';

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
        editDivClass: 'expense-item-edit-div-hide'
    }),
    beforeMount() {
        this.dateConvert();
        this.getTagName();
        this.costToStr();
    },
    methods: {
        dateConvert() {
            let date = new Date(this.expense.date)
            let strDate = date.toString()
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
    .expense-item-edit-div {
        display: flex;
    }
    .expense-item-edit-div-hide {
        display: none;
    }
</style>