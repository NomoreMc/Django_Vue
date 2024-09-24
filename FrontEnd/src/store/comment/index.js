import { createComment, loadComment } from "../../apis/comment";

const comment = {
    state() {
        return {
            commentList: [],
        };
    },
    mutations: {
        initializeCommentList(state, comments) {
            state.commentList = comments;
        }
    },
    actions: {
        async addComment({ commit, dispatch }, { content, postId }) {
            await createComment(content, postId);
            // 评论成功后重新加载评论列表
            dispatch("loadAllComments", postId);
            commit("IncreaseCommentCount", postId);
        },
        async loadAllComments({ commit }, postId) {
            const comments = await loadComment(postId);
            commit("initializeCommentList", comments);
        },
    },
};

export default comment;