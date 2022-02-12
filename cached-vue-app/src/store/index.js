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
    getters: {},
    modules: {}
});

export default store;