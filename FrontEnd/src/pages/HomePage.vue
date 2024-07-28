<template>
    <div class="content">
        <div class="postList">
            <div class="postItem" v-for="n in 10">
                <img src="" alt="" width="100%" height="100%" style="background: #eee" />
                <div class="postInfo">
                    <div class="postMeta">
                        <img src="" alt="" class="avatar" />
                        <span>Nomore</span>
                        <span class="postPubDate">12 hours ago</span>
                        <div class="postActions">
                            <TheIcon icon="like" fill="none" stroke="#000000" />
                            <span>1.5w</span>
                            <TheIcon icon="comment" fill="none" stroke="#000000" />
                            <span>1w</span>
                            <TheIcon icon="favorite" fill="none" stroke="#000000" />
                            <span>99w</span>
                        </div>
                    </div>
                    <div class="postDesc">
                        <p>
                            this is a post description
                            #test #testing #testtest
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import TheIcon from '../components/TheIcon.vue';
</script>

<style scoped>
.content {
    width: 80vw;
    max-width: 1124px;
    margin: 0 auto;
    margin-top: 88px;
}

.postList {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
}

.postItem {
  box-shadow: 0px 12px 24px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
}

.postInfo {
  padding: 24px;
}

.postItem > img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  background: #eee;
  cursor: pointer;
}

.postMeta {
  display: grid;
  grid-template-areas:
    "avatar name actions"
    "pubDate pubDate actions";
  grid-template-columns: 42px 1fr 3fr;
  row-gap: 6px;
}
.postMeta .avatar {
  grid-area: avatar;
}

.postMeta .postPubDate {
  grid-area: pubDate;
  color: #9f9f9f;
  font-size: 14px;
}

.postActions {
  grid-area: actions;
  justify-self: end;
}

.postActions > svg {
  width: 32px;
  height: 32px;
  grid-row: 1 / 2;
}

.postDesc {
  margin-top: 28px;
  white-space: pre-line;
}

.postDetails {
  display: grid;
  grid-template-columns: 1fr minmax(auto, 300px);
  grid-template-rows: minmax(0, 1fr);
  width: 80vw;
  height: 80vh;
}
.postImage {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.postMeta {
  padding: 24px;
  padding-top: 36px;
  display: grid;
  align-items: start;
  grid-template-rows: max-content max-content 1fr max-content;
  max-height: 100%;
  height: 100%;
}

.author {
  display: flex;
  align-items: center;
  gap: 10px;
}
.postDesc {
  width: 100%;
  white-space: pre-wrap;
  margin-top: 24px;
}
.comments {
  display: grid;
  grid-template-columns: 1fr;
  grid-auto-rows: max-content;
  grid-gap: 28px;
  align-items: start;
  overflow-y: auto;
  height: 100%;
}
.comment {
  display: grid;
  grid-template-areas:
    "avatar name date"
    "comment comment comment";
  grid-template-columns: 34px 1fr 1fr;
  align-items: center;
  column-gap: 10px;
  row-gap: 14px;
}
.commentDate {
  grid-area: date;
  justify-self: end;
  color: #a7a7a7;
}
.commentContent {
  grid-area: comment;
}

.actions {
  border-top: 1px solid #eaeaea;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  align-items: center;
  margin: 20px -24px 0px -24px;
  padding: 20px 24px 0 24px;
  row-gap: 16px;
}

.postActions > :deep(svg) {
  transform: scale(0.8125);
}
.postPubDate {
  color: #9f9f9f;
  grid-column: 2 / 6;
  justify-self: end;
  font-size: 14px;
}
.commentInput {
  background: #f7f7f7;
  border-radius: 16px;
  border: none;
  grid-column: 1 / 4;
}
.commentInput::placeholder {
  color: #b9b9b9;
  border: none;
}
.commentPubBtn {
  color: #1da0ff;
  border: none;
  background: none;
  font-size: 16px;
  margin-left: 20px;
  grid-column: 4 / 6;
}
</style>