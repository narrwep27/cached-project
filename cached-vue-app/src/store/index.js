import { createStore } from 'vuex';

const store = createStore({
    state: {
        user: null,
        auth: false
    },
    mutations: {
        setUser(state, payload) {
            state.user = payload.userId;
            state.auth = payload.auth;
        }
    },
    actions: {},
    getters: {},
    modules: {}
});

export default store;