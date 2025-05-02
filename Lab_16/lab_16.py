import face_recognition
known_face = face_recognition.load_image_file("base_image.jpg")
face_1 = face_recognition.load_image_file("face_1.jpg")
face_2 = face_recognition.load_image_file("face_2.jpg")

known_encoding = face_recognition.face_encodings(known_face)[0]
face_1_encoding = face_recognition.face_encodings(face_1)[0]
face_2_encoding = face_recognition.face_encodings(face_2)[0]


result_1 = face_recognition.compare_faces([known_encoding], face_1_encoding)
result_2 = face_recognition.compare_faces([known_encoding], face_2_encoding)

print(f"Первое лицо: {result_1}")
print(f"Второе лицо: {result_2}")