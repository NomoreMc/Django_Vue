
// 暂不使用
export async function uploadFile(file) {
    return null;
    const formData = new FormData();
    formData.append("files", file);

    const response = await fetch("http://localhost:3000/upload", {
        method: "POST",
        body: formData,
        headers: {
            // "Content-Type": "multipart/form-data",
            authorization: `Token ${localStorage.getItem("token")}`,
        },
    });

    const result = await response.json();
    return result[0].url;
}

