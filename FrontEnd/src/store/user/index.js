import { changeUser } from "../../apis/user";
import { getUser, register, login } from "../../apis/auth";

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
        async registerUser({commit}, { username, password, email }) {
            /* 调用 api 向后端发送用户注册请求 */
            const user = await register(username, password, email);
            commit("setUser", user);
        },
        async loginUser({ commit }, { username, password }) {
            /* 调用 api 向后端发送用户登录请求 */
            const user = await login(username, password);
            commit("setUser", user);
        },
        async updateUser({ commit }, user) {
            const updatedUser = await changeUser(user);
            commit("setUser", updatedUser);
        },
    },
};

export default user;