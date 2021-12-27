<template>
  <v-app-bar  :clipped-left="true"  color="white" app>
    <v-app-bar-nav-icon title="Main Menu" @click="ChangeDrawer_mixin(!ComputedDrawer)"></v-app-bar-nav-icon>

    <v-toolbar-title>Academic Media</v-toolbar-title>
  </v-app-bar>
</template>

<script>
import { SkeletonMixins } from "../../mixins/skeleton";

export default {
      mixins: [SkeletonMixins],

};
</script>

<style>
</style>