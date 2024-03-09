<template>
    <template v-if="userStore.user.isAuthenticated" class="flex justify-center items-center">
      <div class="flex justify-center items-center mt-10">
        <div class="w-20 h-20 bg-gray-900 rounded-full"></div>
        <h1 class="ml-64"><strong>{{ user.username }}</strong></h1>
      </div>  
      <div class="flex flex-row justify-center mt-8" v-if="user.id">
        <p class="mr-4 font-bold">
          {{ user.posts_count }} Posts
        </p>
        <RouterLink :to="{ name: 'followers', params: { 'id': user.id }}"
        class="font-bold"
        >
          {{ user.followers_count }} Followers
        </RouterLink>
        <RouterLink
          :to="{ name: 'following', params: { 'id': user.id }}"
          class="ml-4 font-bold"
        >
          {{ user.following_count }} Following
        </RouterLink>
      </div>
      <div class="flex justify-center">
        <button
          class="py-2 px-2 mb-5 mt-5 bg-black text-white rounded-2xl w-96"
          v-if="userStore.user.id !== user.id"
          @click="toggleFollow"
        >
          {{ user.is_following ? 'Following' : 'Follow' }}
        </button>
    
        <button
          class="py-2 px-2 mb-5 mt-5 bg-black text-white rounded-2xl w-96"
          v-else
        >
          Edit profile
        </button>
      </div>
      <div class="flex justify-center mt-5">
        <hr class="w-[500px] h-0.5 mx-auto bg-gray-100 border-0 rounded my-3 dark:bg-black mb-5">
      </div>
  
    </template>
    <template v-else>
      <h1><strong>Please Login to see the profile page</strong></h1>
    </template>

    <Feed/>
  </template>
  
  <script>
  import { useUserStore } from "@/store/user";
  import { useToastStore } from "@/store/toast";
  import Feed from "@/components/Feed.vue";
  import axios from "axios";
  export default {
    setup() {
      const userStore = useUserStore();
      const toastStore = useToastStore();
  
      return {
        userStore,
        toastStore,
      };
    },
    data() {
      return {
        user: {
          id: "",
          is_following: false,
        },
        posts: [],

      };
    },
    components: {
      Feed
    },
    mounted() {
      this.getUser();
      this.getUserPosts();
    },
    watch: {
      "$route.params.id": {
        handler: function () {
          this.getUser();
        },
        deep: true,
        immediate: true,
      },
    },
    methods: {
    getUser() {
      axios
        .get(`/api/profile/${this.$route.params.id}/`)
        .then((response) => {
          this.user = response.data.user;
          this.user.is_following = response.data.is_following;
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    getUserPosts(){
      axios
          .get(`/api/posts/profile/${this.$route.params.id}/`)
          .then(response => {
            this.posts = response.data.posts
            this.user = response.data.user
          })
          .catch(error => {
            console.log('error', error)
          })
    },
    toggleFollow() {
      if (this.user.is_following) {
        this.unfollowUser();
      } else {
        this.followUser();
      }
    },
    followUser() {
      axios
        .post(`/api/following/${this.$route.params.id}/follow/`)
        .then((response) => {
          this.user.is_following = true;
          console.log("Followed", response.data);
          this.user.followers_count += 1
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
    unfollowUser() {
      axios
        .post(`/api/following/${this.$route.params.id}/unfollow/`)
        .then((response) => {
          this.user.is_following = false;
          this.user.followers_count -= 1
          console.log("Unfollowed", response.data);
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
  },
  };
  </script>
  