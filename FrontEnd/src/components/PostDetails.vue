<template>
  <TheModal @close="$store.dispatch('hidePostDetails')">
    <div class="postDetails">
      <img class="postImage" src="../assets/background.png" alt="" />
      <div class="postMeta">
        <div class="author">
          <TheAvatar />
          <span>{{ post?.author?.username }}</span>
        </div>
        <pre class="postDesc">
{{ post?.content }}
        </pre>
        <div class="comments">
          <div class="comment" v-for="comment in comments">
            <TheAvatar src="../assets/avatarDefault.png"/>
            <span class="user">{{ comment?.author?.username }}</span>
            <span class="commentDate">{{ dateToRelative(comment.create_time) }}</span>
            <p class="commentContent">{{ comment.content }}</p>
          </div>
        </div>
        <div class="actions">
          <PostActions
            :likes="post.likes"
            :comments="post.comments"
            :favors="post.favors"
            :likedByMe="post.likedByMe"
            :favoredByMe="post.favoredByMe"
            @likeClick="$store.dispatch('toggleLike', post.id)"
            @favorClick="$store.dispatch('toggleFavor', post.id)"
          />
          <span class="postPubDate">{{ dateToRelative(post.date_posted) }}</span>
          <input
            type="text"
            name="comment"
            id=""
            class="commentInput"
            placeholder="写一条评论吧！"
            v-model="commentContent"
          />
          <button @click="store.dispatch('addComment', { commentContent, postId: post.id })" class="commentPubBtn">发布</button>
        </div>
      </div>
    </div>
  </TheModal>
</template>

<script setup>
import TheAvatar from "./TheAvatar.vue";
import TheIcon from "./TheIcon.vue";
import PostActions from "./PostActions.vue";
import TheModal from "./TheModal.vue";
import { useStore } from "vuex";
import { computed, ref } from "vue";
import { dateToRelative } from "../utils/date";

const commentContent = ref("");

const store = useStore();
const post = computed(() => store.getters.postDetails);
const comments = computed(() => store.state.comment.commentList);

</script>

<style scoped>
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

.postActions > :deep(svg) {
  transform: scale(0.8125);
}
</style>
