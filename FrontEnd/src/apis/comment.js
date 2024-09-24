import { request } from "../utils/request";

// 暂未启用，后端未实现
export async function createComment(content, postId) {
    return true;
    await request("/Comment/api/comment/create/", {
        method: "POST",
        body: {
            content,
            post: postId,
        },
        headers: {
            "Authorization": `Token ${getToken()}`,
        }
    });
};

export async function loadComment(postId) {
    return [];
    if (!postId) {
        return [];
    }

    // URL 路径需要进一步确认
    const response = await request("/Comment/api/comment/comments?populate=*&filters[post][id][$eq]=" + postId);

    // 后端返回的数据有待考究
    return response.map((comment) => ({
        content: comment?.content,
        create_time: comment?.create_time,
        author: {
            id: comment?.author?.id,
            username: comment?.author?.username,
            email: comment?.author?.email,
        },
        post: {
            id: comment?.post?.id,
            title: comment?.post?.title,
            content: comment?.post?.content,
            date_posted: comment?.post?.date_posted,
        },
        parent_comment: comment?.parent_comment,
    }));
};