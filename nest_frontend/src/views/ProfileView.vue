<template>
    <template v-if="userStore.user.isAuthenticated">
      <h1><strong>{{ user.username }}</strong></h1>
      <div class="flex flex-row justify-center" v-if="user.id">
        <RouterLink to='#' class="mr-4">
          {{ user.posts_count }} Posts
        </RouterLink>
        <RouterLink :to="{ name: 'followers', params: { 'id': user.id }}">
          {{ user.followers_count }} followers
        </RouterLink>
        <RouterLink
          :to="{ name: 'following', params: { 'id': user.id }}"
          class="ml-4"
        >
          {{ user.following_count }} following
        </RouterLink>
      </div>
  
      <button
        class="py-2 px-2 bg-gray-500 rounded-xl"
        v-if="userStore.user.id !== user.id"
        @click="toggleFollow"
      >
        {{ user.is_following ? 'Unfollow' : 'Follow' }}
      </button>
  
      <button
        class="py-2 px-2 bg-gray-500 rounded-xl"
        v-else
      >
        Edit profile
      </button>
  
    </template>
    <template v-else>
      <h1><strong>Please Login to see the profile page</strong></h1>
    </template>
  </template>
  
  <script>
  import { useUserStore } from "@/store/user";
  import { useToastStore } from "@/store/toast";
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
      };
    },
    mounted() {
      this.getUser();
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
  