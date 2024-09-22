<template>
  <div class="postActions">
    <TheIcon icon="like"
      :fill="likedByMe ? '#FF3C3C' : 'none'"
      :stroke="likedByMe ? '#FF3C3C' : '#000000'"
      @click="emit('likeClick')"/>
    <span>{{ likes || "" }}</span>
    <TheIcon icon="comment"
      fill="none"
      stroke="#000000"
      @click="emit('commentClick')"/>
    <span>1w</span>
    <TheIcon icon="favorite"
      :fill="favoredByMe ? '#FFD12E' : 'none'"
      :stroke="favoredByMe ? '#FFD12E' : '#000000'"
      @click="emit('favorClick')"/>
    <span>{{ favors || "" }}</span>
  </div>
</template>
<script setup>
import TheIcon from "./TheIcon.vue";
import { defineProps, defineEmits } from "vue";

defineProps({
    likes: Number,
    comments: Number,
    favors: Number,
    likedByMe: Boolean,
    favoredByMe: Boolean,
});

const emit = defineEmits([
  "likeClick",
  "commentClick",
  "favorClick",
]);
</script>

<style scoped>
.postActions {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  justify-items: center;
  column-gap: 16px;
  row-gap: 4px;
}

.postActions > svg {
  width: 32px;
  height: 32px;
  grid-row: 1 / 2;
  cursor: pointer;
}

.postActions > span {
  font-size: 14px;
}
</style>
