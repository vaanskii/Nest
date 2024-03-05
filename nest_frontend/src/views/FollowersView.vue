<template>
    <div v-if="followers.length">
        <div
            v-for="user in followers"
            v-bind:key="user.id"    
            >
            <RouterLink :to="{name: 'profile', params: {'id': user.id}}">{{ user.username }}</RouterLink>
        </div>
    </div>
    <div v-else>
        No followers
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
            followers: [],
        }
    },
    mounted() {
        this.getFollowersList()
    },
    methods: {
        getFollowersList() {
            axios
                .get(`/api/followers/${this.$route.params.id}/`)
                .then(response => {
                    this.followers = response.data.followers
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>