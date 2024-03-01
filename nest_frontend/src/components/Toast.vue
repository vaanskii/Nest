<script setup>
import { useToastStore } from '@/store/toast'

const store = useToastStore()
</script>

<template>
    <div
        v-if="store.isVisible"
        class="transition ease-in-out delay-1000 duration-1000 px-6 py-6 mt-[-25px] fixed rounded-xl shadow-xl"
        :class="store.classes"
    >
        {{ store.message }}
    </div>
</template>