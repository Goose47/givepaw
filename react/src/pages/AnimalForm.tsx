import React, { useEffect, useState } from "react";
import type { RadioChangeEvent } from "antd";
import { Button, Input, Radio, Select, Space } from "antd";
import { Checkbox } from 'antd';

import { useDispatch, useSelector } from "react-redux";
import { fetchPets, selectPets } from "../redux/slices/PetsSlice";
import { getAnimalTypes, getBloodTypes, getBreeds, getComponentTypes, getVaccines } from "../service/data.service";
import { selectUser } from "../redux/slices/UserSlice";
import MyPetSelect from "../components/Forms/MyPetSelect";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import UploadPhoto from "../components/global/UploadPhoto";

const AnimalForm = (props: any) => {
  const [animalType, setAnimalType] = useState("");
  const [breed, setBreed] = useState("");
  const [bloodGroup, setBloodGroup] = useState("");
  const [petName, setPetName] = useState("");
  const [bloodComponent, setBloodComponent] = useState("");
  const [image, setImage] = useState("");
  const [age, setAge] = useState("");
  const [weight, setWeight] = useState("");
  const [vaccinations, setVaccinations] = useState<any[]>([]);
  const [vaccinationsOptions, setVaccinationsOptions] = useState([]);
  const user = useSelector(selectUser);

  const [breedOptions, setBreedOptions] = useState<any[]>([]);
  const [animalTypeOptions, setAnimalTypeOptions] = useState<any[]>([]);
  const [bloodComponentOptions, setBloodComponentOptions] = useState<any[]>([]);
  const [bloodGroupOptions, setBloodGroupOptions] = useState<any[]>([]);

  const handleSelectChange = (value: any) => {
    setBreed(value);
  };

  const onChangeAnimalType = async (e: RadioChangeEvent) => {
    const value = e.target.value;
    setAnimalType(value);

    const breeds = await getBreeds(value);
    setBreedOptions(breeds);

    const bloodTypes = await getBloodTypes(value);
    setBloodGroupOptions(bloodTypes);
  };

  const onChangeBloodGroup = (e: RadioChangeEvent) => {
    setBloodGroup(e.target.value);
  };

  const onChangeComponentType = (e: RadioChangeEvent) => {
    setBloodComponent(e.target.value);
  };

  const handleImageChange = (event: any) => {
    const file = event.target.files[0];
    setImage(file);
  };

  const [error, setError] = useState<string>();
  const { id } = useParams()

  const handleSend = () => {
    if (!animalType) {
      setError("Неверно указан тип животного");
    } else if (!breed) {
      setError("Неверно указана порода животного");
    } else if (!bloodGroup) {
      setError("Неверно указана группа крови");
    } else if (!petName) {
      setError("Неверно указано имя питомца");
    } else if (!age) {
      setError("Неверно указан возраст питомца");
    } else if (!weight) {
      setError("Неверно указан вес питомца");
    } else if (vaccinesDates.filter((el) => !el).length) {
      setError("Неверно указаны даты вакцинаций");
    } else {
      setError(undefined);
      let vaccines = []
      for (let i = 0; i < vaccinesDates.length; i++) {
        vaccines.push({
          vaccination_id: selectedVaccines[i],
          vaccination_date: vaccinesDates[i],
        })
      }
      axios.post("pets/", {
        "blood_group_id": bloodGroup,
        "breed_id": breed,
        "breed": null,
        "pet_type_id": animalType,
        "avatar": avatar,
        "name": petName,
        "age": age,
        "weight": weight,
        "vaccinations": vaccines
      }).then(response => {
        if (props.mode === "donor") {
          navigate("/donor/" + response.data.id);
        } else if (props.mode === "recipient") {
          navigate("/recipient/" + response.data.id);
        } else {
          navigate("/respond/" + response.data.id + "/" + id);
        }
      }).catch(error => {
        if (error.response.status === 400) {
          alert(error.response.data.detail);
        }
      });
    }

  };

  useEffect(() => {
    const fetchData = async () => {
      const animalTypes = await getAnimalTypes();
      setAnimalTypeOptions(animalTypes);

      const components = await getComponentTypes();
      setBloodComponentOptions(components);

      const vaccinesOptions = await getVaccines();
      setVaccinationsOptions(vaccinesOptions);

    };

    fetchData();
  }, []);

  const [selectedPetId, setSelectedPetId] = useState<number>();
  const [selectingPetId, setSelectingPetId] = useState<boolean>(false);

  const [avatar, setAvatar] = useState<any>(null);

  const dispatch = useDispatch();
  const pets = useSelector(selectPets);

  useEffect(() => {
    dispatch(fetchPets() as any);
  }, [dispatch]);

  useEffect(() => {
    if (pets?.length > 0 && !selectingPetId && !selectedPetId) {
      setSelectingPetId(true);
    }
  }, [pets]);

  const handleAppend = () => {
    console.log(vaccinationsOptions);
    setSelectingPetId(false);
  };

  const navigate = useNavigate();

  const handleSelect = (value: number) => {
    setSelectedPetId(value);
    setSelectingPetId(false);
    if (props.mode === "donor") {
      navigate("/donor/" + value);
    } else if (props.mode === "recipient") {
      navigate("/recipient/" + value);
    } else {
      navigate("/respond/" + value + '/' + id);
    }
  };

  const [selectedVaccines, setSelectedVaccines] = useState<number[]>([]);
  const [vaccinesDates, setVaccinesDate] = useState<string[]>([]);

  useEffect(() => {
    let vaccinesDatesCopy = JSON.parse(JSON.stringify(vaccinesDates))
    while (vaccinesDatesCopy.length < selectedVaccines.length) {
      vaccinesDatesCopy.push("")
    }
    while (vaccinesDatesCopy.length > selectedVaccines.length) {
      vaccinesDatesCopy.pop()
    }
    setVaccinesDate(vaccinesDatesCopy)
  }, [selectedVaccines]);

  const handleSelectVaccines = (vaccines: any) => {
    setSelectedVaccines(vaccines);
  };

  const handleUpdateVaccineById = (id: number, e: any) => {
    console.log(selectedVaccines, vaccinesDates)
    let vaccineDatesCopy = JSON.parse(JSON.stringify(vaccinesDates))
    for (let i = 0; i < selectedVaccines.length; i++) {
      if (selectedVaccines[i] === id) {
        vaccineDatesCopy[i] = e.target.value
      }
    }
    setVaccinesDate(vaccineDatesCopy)
  }

  return (
    <div>
      {
        props.mode === "donor" ? (
          <h1>Форма донора</h1>
        ) : (props.mode === 'recipient' ? (
          <h1>Форма реципиента</h1>
        ) : (
          <h1>Срочный сбор крови</h1>
        ))
      }
      {
        selectingPetId && <MyPetSelect onAppend={handleAppend} onSelect={handleSelect} />
      }
      <div className="Form">
        {
          !selectingPetId && (
            <>
              {animalTypeOptions && (
                <>
                  <div>Тип животного</div>
                  <Radio.Group onChange={onChangeAnimalType} defaultValue="a">
                    {animalTypeOptions.map((animalType) => (
                      <Radio.Button key={animalType.id} value={animalType.id}>
                        <span style={{ display: 'flex', alignItems: 'center' }}>
                        <img style={{
                          width: 20,
                          height: 20,
                          marginRight: 5,
                        }} src={animalType.icon} alt="#" /> {animalType.title}
                          </span>
                      </Radio.Button>
                    ))}
                  </Radio.Group>
                </>
              )}
              {bloodGroupOptions.length > 1 && (
                <div className="Form__Element">
                  <div>Группа крови</div>
                  <Radio.Group onChange={onChangeBloodGroup} defaultValue="a">
                    {bloodGroupOptions.map((bloodGroup) => (
                      <Radio.Button key={bloodGroup.id} value={bloodGroup.id}>
                        {bloodGroup.blood_group.title}, {bloodGroup.rhesus.title}
                      </Radio.Button>
                    ))}
                  </Radio.Group>
                </div>
              )}
              <div className="Form__Element">
                {breedOptions.length > 0 && (
                  <Select
                    id="breed"
                    placeholder="Порода"
                    onChange={handleSelectChange}
                    options={breedOptions.map((breed) => ({ value: breed.id, label: breed.title }))}
                  />
                )}
              </div>
              <label htmlFor="name">Кличка</label>
              <Input
                id="name"
                placeholder="Кличка"
                value={petName}
                type="text"
                onChange={(e) => setPetName(e.target.value)}
              />

              <label htmlFor="age">Возраст</label>
              <Input id="age" placeholder="Возраст" value={age} type="text" onChange={(e) => setAge(e.target.value)} />

              <label htmlFor="weight">Вес</label>
              <Input id="weight" placeholder="Вес" value={weight} type="text" onChange={(e) => setWeight(e.target.value)} />

              <label htmlFor="file">Аватар животного</label>
              <UploadPhoto setBase={setAvatar} />

              <div className="Vaccine__Main">
                <Space style={{ width: "100%" }} direction="vertical">
                  <Select
                    mode="multiple"
                    allowClear
                    style={{ width: "100%" }}
                    placeholder="Прививки"
                    onChange={handleSelectVaccines}
                    options={vaccinationsOptions.map((el: any) => {
                      return {
                        value: el.id,
                        label: el.title
                      };
                    })}
                  />
                </Space>
              </div>

              <div className="Vaccines__Dates">
                <div className="Vaccines__Dates__Title">Даты прививок</div>
                {
                  selectedVaccines.map(el => {
                    let currentVaccine: any = vaccinationsOptions.filter((k: any) => k.id == el)[0];
                    return (
                      <div className="Vaccines__Dates__Item">
                        <div>{currentVaccine?.title}</div>
                        <div>
                          <input type="date" onChange={(e: any) => handleUpdateVaccineById(el, e)} />
                        </div>
                      </div>
                    );
                  })
                }
              </div>
              <div>
              <Checkbox onChange={() => {}}><div> Нужна переноска</div></Checkbox>
              </div>
            </>
          )
        }
        {
          error && (<p className={"Error"}>{error}</p>)
        }
        {
          !selectingPetId && (<Button type="primary" onClick={handleSend}>
            Добавить питомца
          </Button>)
        }

      </div>


      {/*{bloodComponentOptions && (*/}
      {/*  <div className="Form__Element">*/}
      {/*    <div>Компонент крови</div>*/}
      {/*    <Radio.Group onChange={onChangeComponentType} defaultValue="a">*/}
      {/*      {bloodComponentOptions.map((component) => (*/}
      {/*        <Radio.Button key={component.id} value={component.id}>*/}
      {/*          {component.title}*/}
      {/*        </Radio.Button>*/}
      {/*      ))}*/}
      {/*    </Radio.Group>*/}
      {/*  </div>*/}
      {/*)}*/}


    </div>
  );
};

export default AnimalForm;
