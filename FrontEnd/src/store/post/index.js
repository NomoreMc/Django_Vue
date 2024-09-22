import { createPost, likePost, loadPost, favorPost } from "../../apis/post";

const post = {
    state() {
        return {
            postList: [],
            currentPostId: null,
        };
    },
    mutations: {
        initializePostList(state, posts) {
            state.postList = posts;
        },
        toggleLike(state, { id, isLike }) {
            const post = state.postList.find((post) => post.id === id);
            /* 直接修改本地已有 post 的值，也可以选择再次请求 all posts */
            if (isLike) {
                post.liked_bies = (post.liked_bies || 0) + 1;
            } else {
                post.liked_bies--;
            }
            post.likedByMe = isLike;
        },
        toggleFavor(state, { id, isFavor }) {
            const post = state.postList.find((post) => post.id === id);
            /* 直接修改本地已有 post 的值，也可以选择再次请求 all posts */
            if (isFavor) {
                post.favored_bies = (post.favored_bies || 0) + 1;
            } else {
                post.favored_bies--;
            }
            post.favoredByMe = isFavor;
        },
        setCurrentPostId(state, id) {
            state.currentPostId = id;
        },
    },
    actions: {
        async uploadPost({ commit, dispatch }, { image, title, description }) {
            await createPost(image, title, description);

            dispatch("loadAllPosts");
            /* 上传成功后关闭弹窗 */
            commit("changeShowPostUpload", false);
        },
        async loadAllPosts({ commit }) {
            const posts = await loadPost();
            commit("initializePostList", posts);
        },
        async toggleLike({ commit }, id) {
            const isLike = await likePost(id);
            commit("toggleLike", { id, isLike });
        },
        async toggleFavor({ commit }, id) {
            const isFavor = await favorPost(id);
            commit("toggleFavor", { id, isFavor });
        },
        async showPostDetails({ commit }, id) {
            commit("setCurrentPostId", id);
            commit("changeShowPostDetails", true);
        },
        async hidePostDetails({ commit }) {
            commit("setCurrentPostId", null);
            commit("changeShowPostDetails", false);
        },
    },
    getters: {
        postDetails(state) {
            return state.postList.find((post) => post.id === state.currentPostId);
        },
    },
};

export default post;