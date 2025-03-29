<template>
    <div v-if="store.user.isAuthenticated">
        <Feed/>
    </div>
    <div v-else>
        <LoginView />
    </div>
</template>

<script>
import Feed from '@/components/Feed.vue';
import { useUserStore } from '@/store/user';
import LoginView from './LoginView.vue';

export default {
    setup() {
        const store = useUserStore()

        return {
            store
        }
    },

    components: {
        Feed,
        LoginView
    },
}
</script>