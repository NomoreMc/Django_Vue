import { getToken, getUser } from "./auth";
import { request } from "../utils/request";

export async function createPost(image, title, description) {
    const formData = new FormData();
    // formData.append("files.image", image);
    // formData.append("title", title);
    // formData.append("content", description);

    const result = await request("/Post/api/post/create/", {
        method: "POST",
        // body: formData,
        body: {
            title: title,
            content: description,
        },
        headers: {
            // "Content-Type": "multipart/form-data",
            "Authorization": `Token ${getToken()}`,
        },
    });
}

// TODO：要修改 loadPosts 函数，使其支持筛选条件，当前后端未提供筛选条件
export async function loadPosts(filters = "") {
    // const result = await request("/Post/api/post/list/" + (filters && `&${filters}`), {
    const result = await request("/Post/api/post/list/", {
        method: "GET",
        headers: {
            "Authorization": `Token ${getToken()}`,
        },
    });

    return result.map((post) => ({
        id: post?.id,
        title: post?.title,
        content: post?.content,
        // image: post?.image,
        date_posted: post?.date_posted,
        author: {
            id: post?.author?.id,
            username: post?.author?.username,
            email: post?.author?.email,
        },
        // 以下字段暂不存在
        likes: 0,
        liked_bies: 0,
        likedByMe: false,
        favors: 0,
        favored_bies: 0,
        favoredByMe: false,
        comments: 0,
    }));
}

// 加载我发布的 post，需要修改
export async function loadPostsByMe() {
    return loadPosts(`filters[user][id][$eq]=${getUser().id}`);
}

// 加载我点赞过的 post，需要修改
export async function loadPostsLikedOrFavoredByMe(type = "likes") {
    return null;
    const response = await request(
        `/Account/me?populate[${type}][populate][0]=image`,
        {
            method: "GET",
            headers: {
                Authorization: `Token ${getToken()}`,
            },
        });
    return response[type].map((post) => ({
        ...post,
        image: post?.image?.[0].url,
    }));
}

/* post 点赞 */
export async function likePost(postId) {
    // 暂时写死，后端暂未实现
    return true;
    const result = await request(`/Post/api/post/${postId}/like/`, {
        method: "PUT",
        headers: {
            "Authorization": `Token ${getToken()}`,
        },
    });

    /* 返回 isLike 字段值，true 为点赞， false 为取消点赞 */
    return result.data;
}

/* post 收藏 */
export async function favorPost(postId) {
    // 暂时写死，后端暂未实现
    return true;
    const result = await request(`/Post/api/post/${postId}/favor/`, {
        method: "PUT",
        headers: {
            "Authorization": `Token ${getToken()}`,
        },
    });
    return result.data;
}