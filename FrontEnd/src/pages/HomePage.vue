<template>
    <div>
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
</style>