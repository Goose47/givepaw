import axios from 'axios';

export const register = async (
  username: string,
  name: string,
  phone: string,
  surname: string,
  patronymic: string,
  email: string,
  password: string,
  city: number,
  image: any
) => {
  try {
    const response = await axios.post('auth/register', {
      'username': username,
      'name': name,
      'phone': phone,
      'surname': surname,
      'patronymic': patronymic,
      'email': email,
      'password': password,
      'city_id': city.toString(),
      'avatar': image
    });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const login = async (username: string, password: string) => {
  try {
    const response = await axios.post('auth/login', { username, password });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
