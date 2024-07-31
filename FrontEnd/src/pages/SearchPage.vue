<template>
    <div>
        <h2 class="title">搜索结果：植物</h2>
        <PostList>
            <PostItem v-for="n in 10" />
        </PostList>
        <!-- <PostDetails /> -->
        <!-- <PostUpload /> -->
    </div>
</template>

<script setup>
import PostList from '../components/PostList.vue';
import PostItem from '../components/PostItem.vue';
import PostDetails from '../components/PostDetails.vue';
import PostUpload from '../components/PostUpload.vue';
</script>

<style scoped>
.title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 44px;
}
</style>