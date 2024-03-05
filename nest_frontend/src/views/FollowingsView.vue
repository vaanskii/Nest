<template>
    <div v-if="following.length">
        <div
            v-for="user in following"
            v-bind:key="user.id"    
            >
            <RouterLink :to="{name: 'profile', params: {'id': user.id}}">{{ user.username }}</RouterLink>
        </div>
    </div>
    <div v-else>
        No followings
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/store/user'
export default{
    setup() {
        const userStore = useUserStore()

        return {
            userStore,
        }
    },
    data() {
        return {
            user: {},
            following: [],
        }
    },
    mounted() {
        this.getFollowingList()
    },
    methods: {
        getFollowingList() {
            axios
                .get(`/api/following/${this.$route.params.id}/`)
                .then(response => {
                    this.following = response.data.following
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>