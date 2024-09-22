import { createStore } from 'vuex';

import user from './user/index';
import post from './post/index';
import comment from './comment/index';

export const store = createStore({
    modules: {
        user,
        post,
        comment,
    },
    state() {
        return {
            showPostUpload: false,  /* Post Create 弹窗 */
            showPostDetails: false,  /* Post 详情弹窗 */
        };
    },
    mutations: {
        changeShowPostUpload(state, show) {
            state.showPostUpload = show;
        },
        changeShowPostDetails(state, show) {
            state.showPostDetails = show;
        },
    },
    actions: {},
});