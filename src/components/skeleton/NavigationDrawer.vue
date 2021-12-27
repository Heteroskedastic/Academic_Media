<template>
  <v-navigation-drawer floating clipped width="280" v-model="ComputedDrawer" app>
    <!--  -->
    <v-list  rounded dense>
      <!-- <v-subheader>REPORTS</v-subheader> -->
      <v-list-item-group v-model="value" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { SkeletonMixins } from "../../mixins/skeleton";

export default {
  mixins: [SkeletonMixins],
  data() {
    return {
        value: '',
      items: [
        { text: "stories", icon: "mdi-web" },
      ],
    };
  },
};
</script>

<style>
</style>