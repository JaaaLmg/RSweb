import { defineStore } from "pinia";

export const mainStore = defineStore("main", {
  state: () => {
    return {
      helloPinia:'你好 Pinia!'
    };
  },
  getters: {},
  actions: {},  
});