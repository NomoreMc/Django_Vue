import { getUser, register } from "../../apis/auth";

const user = {
    state() {
        return {
            user: getUser() || {},
        };
    },
    mutations: {
        setUser(state, user) {
            state.user = user;
        },
    },
    actions: {
        async registerUser({commit}, { email, username, password }) {
            /* 调用 api 向后端发送用户注册请求 */
            const user = await register(email, username, password);
            commit("setUser", user);
        },
    },
};

export default user;