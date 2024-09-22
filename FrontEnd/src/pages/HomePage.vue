<template>
    <div>
        <PostList>
            <PostItem v-for="post in posts" :post="post" :key="post.id" />
        </PostList>
        <PostDetails v-if="showPostDetails"/>
        <PostUpload v-if="showPostUpload"/>
    </div>
</template>

<script setup>
import PostList from '../components/PostList.vue';
import PostItem from '../components/PostItem.vue';
import PostDetails from '../components/PostDetails.vue';
import PostUpload from '../components/PostUpload.vue';
import { useStore } from 'vuex';
import { computed } from 'vue';
import { onMounted } from 'vue';

const store = useStore();
const showPostUpload = computed(() => store.state.showPostUpload);
const showPostDetails = computed(() => store.state.showPostDetails);
const posts = computed(() => store.state.post.postList);

/* 生命周期钩子：在组件挂载之后就触发加载 post action */
onMounted(() => {
    store.dispatch('loadAllPosts');
});

</script>

<style scoped>
</style>