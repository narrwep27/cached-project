import { createStore } from 'vuex';

const store = createStore({
    state: {
        auth: false,
        userId: null,
        email: '',
        tags: [],
        expenses: [],
        goals: []
    },
    mutations: {
        setUser(state, payload) {
            state.auth = payload.auth;
            state.userId = payload.userObj.id;
            state.email = payload.userObj.email;
            state.tags = payload.userObj.tags;
            state.expenses = payload.userObj.expenses;
            state.goals = payload.userObj.goals;
        },
        setTags(state, payload) {
            state.tags = payload
        },
        setExpenses(state, payload) {
            state.expenses = payload
        },
        setGoals(state, payload) {
            state.goals = payload
        },
        clearUser(state) {
            state.auth = false,
            state.userId = null,
            state.email = '',
            state.tags = [],
            state.expenses = [],
            state.goals = []
        }
    },
    actions: {},
    getters: {
        sortExpensesByDate(state) {
            let sortedExpenses = state.expenses.sort((a, b) => {
                let aDate = new Date(a.date);
                let bDate = new Date(b.date);
                return bDate - aDate;
            });
            return sortedExpenses;
        }
    },
    modules: {}
});

export default store;