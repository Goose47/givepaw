import { configureStore } from '@reduxjs/toolkit';
import userReducer from './slices/UserSlice';
import petsReducer from './slices/PetsSlice';
import socialReducer from './slices/SocialSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
    pets: petsReducer,
    social: socialReducer
  },
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;
