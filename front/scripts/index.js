window.onload = (event) => {
  console.log("page is fully loaded");
  createTable();
  getCandidates();
};

// Enums
const GenderEnum = {
  0: "Feminine",
  1: "Masculine",
};

const EducationLevelEnum = {
  1: "Bachelor's (Type 1)",
  2: "Bachelor's (Type 2)",
  3: "Master's",
  4: "PhD",
};

const RecruitmentStrategyEnum = {
  1: "Aggressive",
  2: "Moderate",
  3: "Conservative",
};

const HiringDecisionEnum = {
  0: "Not Hired",
  1: "Hired",
};

const TABLE_ATTRIBUTE_ORDER = [
  "Id",
  "E-mail",
  "Age",
  "Gender",
  "Education Level",
  "Experience Years",
  "Previoous Companies",
  "Company Distance",
  "Interview Score",
  "Skill Score",
  "Personality Score",
  "Recruitment Strategy",
  "Hiring Decision",
  "Edit",
  "Remove",
];

// Set input value by the range or the text input associated
const updateRangeInput = (val, el) => {
  document.getElementById(el).value = val;
};

// Reset values after sucessfully sent to database
const resetInputValue = (data) => {
  for (let elem in data) {
    if (elem == "is_update") {
      data[elem].checked = false;
    } else if (elem == "gender") {
      document.getElementById("radioDefault").checked = true;
    } else {
      data[elem].value = "";
    }
  }
};

// Convert categorical data for display in the table
const convertCategoricalData = (item) => {
  for (let key in item) {
    if (key == "gender") {
      item[key] = GenderEnum[item[key]];
    }

    if (key == "education_level") {
      item[key] = EducationLevelEnum[item[key]];
    }

    if (key == "recruitment_strategy") {
      item[key] = RecruitmentStrategyEnum[item[key]];
    }

    if (key == "hiring_decision") {
      item[key] = HiringDecisionEnum[item[key]];
    }
  }
};

// Create table for display of candidates data
const createTable = () => {
  const tableHead = document.getElementById("tableHead");
  const tr_head = document.createElement("tr");

  for (let att in TABLE_ATTRIBUTE_ORDER) {
    const th_head = document.createElement("th");
    th_head.setAttribute("scope", "col");
    th_head.innerText = TABLE_ATTRIBUTE_ORDER[att];
    tr_head.appendChild(th_head);
  }

  tableHead.appendChild(tr_head);
};

// Create a remove button for the table row
const createRemoveBtn = (id) => {
  const remove = document.createElement("span");
  remove.style.color = "red";
  remove.style.border = "1px solid red";
  remove.style.padding = "3px";
  remove.innerText = "X";
  const tdRemove = document.createElement("td");
  tdRemove.appendChild(remove);
  tdRemove.addEventListener("click", async () => removeItem(id));
  return tdRemove;
};

// Create a edit button for the table row
const createEditBtn = (parent) => {
  const edit = document.createElement("span");
  edit.style.color = "blue";
  edit.style.border = "1px solid blue";
  edit.style.padding = "3px";
  edit.innerText = "\u2B6B";
  const tdEdit = document.createElement("td");
  tdEdit.appendChild(edit);
  tdEdit.addEventListener("click", async () => editItem(parent));

  return tdEdit;
};

// To insert candidate data in the display table
const insertRow = (item) => {
  const tableBody = document.getElementById("tableBody");
  const id = item.id;

  const is_hired = item.hiring_decision == "Hired" ? true : false;

  // Need to keep order for table data
  const data = [
    item.email,
    item.age,
    item.gender,
    item.education_level,
    item.xp_years,
    item.prev_cia_worked,
    item.dist_cia,
    item.interview_score,
    item.skill_score,
    item.personality_score,
    item.recruitment_strategy,
    item.hiring_decision,
  ];

  const trBody = document.createElement("tr");
  const thBody = document.createElement("th");

  thBody.setAttribute("scope", "row");
  thBody.innerText = id;

  trBody.appendChild(thBody);

  data.forEach((elem, idx, array) => {
    const tdBody = document.createElement("td");
    tdBody.innerText = elem;
    if (idx === array.length - 1 && is_hired) {
      tdBody.style.color = "blue";
      tdBody.style.fontWeight = 600;
      tdBody.style.fontSize = "large";
      tdBody.style.backgroundColor = "lightblue";
    }
    if (idx === array.length - 1 && !is_hired) {
      tdBody.style.color = "red";
      tdBody.style.backgroundColor = "lavenderblush";
    }
    trBody.appendChild(tdBody);
  });

  const tdEdit = createEditBtn(trBody);
  trBody.appendChild(tdEdit);
  const tdRemove = createRemoveBtn(id);
  trBody.appendChild(tdRemove);

  tableBody.appendChild(trBody);
};

// To request candidate data from database
const getCandidates = async () => {
  const url = "http://127.0.0.1:5000/candidate";

  fetch(url, {
    method: "get",
  })
    .then((response) => response.json())
    .then((data) => {
      data.candidates.forEach((item) => {
        convertCategoricalData(item);
        insertRow(item);
      });
    })
    .catch((error) => {
      console.error("Error", error);
    });
};

// Send dataform to Prediction and Insertion/Update in database
const dataForm = document.getElementById("dataForm");
dataForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const url = "http://127.0.0.1:5000/candidate";

  // Get input elements to set a formdata
  const data = {
    email: document.getElementById("candidateEmail"),
    age: document.getElementById("rangeAgeInput"),
    gender: Array.from(document.getElementsByName("genderRadioInput")).find(
      (radio) => radio.checked
    ),
    education_level: document.getElementById("educationSelect"),
    xp_years: document.getElementById("rangeXpInput"),
    prev_cia_worked: document.getElementById("rangePrevCiaInput"),
    dist_cia: document.getElementById("rangeDistCiaInput"),
    interview_score: document.getElementById("rangeInterviewScoreInput"),
    skill_score: document.getElementById("rangeSkillScoreInput"),
    personality_score: document.getElementById("rangePersonalityScoreInput"),
    recruitment_strategy: document.getElementById("strategySelect"),
  };

  // Add check in formdata if it is an update
  const isToUpdate = document.getElementById("checkToUpdate");
  if (isToUpdate.checked) {
    data["is_update"] = isToUpdate;
  }

  const formData = new FormData();

  for (let elem in data) {
    if (data[elem].value == "") {
      alert(`${elem} is required!`);
      return;
    } else {
      formData.append(elem, data[elem].value);
    }
  }

  const response = await fetch(url, {
    method: "post",
    body: formData,
  });

  const responseJson = await response.json();
  const responseStatus = await response.status;

  if (responseStatus == 200) {
    resetInputValue(data);
    location.reload();
  } else {
    alert(`Não foi possivel realizar a predição com o modelo e nem inserir na base de dados. 
      Status: ${responseStatus}.
      Resposta: ${responseJson.message}`);
  }
});

// To set candidates data in the input for data update
const editItem = (parent) => {
  const children = parent.children;
  const elemListOrder = [
    null, // ID index from table not used
    document.getElementById("candidateEmail"),
    document.getElementById("rangeAgeInput"),
    null, // Gender index from table not necessary
    document.getElementById("educationSelect"),
    document.getElementById("rangeXpInput"),
    document.getElementById("rangePrevCiaInput"),
    document.getElementById("rangeDistCiaInput"),
    document.getElementById("rangeInterviewScoreInput"),
    document.getElementById("rangeSkillScoreInput"),
    document.getElementById("rangePersonalityScoreInput"),
    document.getElementById("strategySelect"),
  ];

  for (let col in TABLE_ATTRIBUTE_ORDER) {
    if (TABLE_ATTRIBUTE_ORDER[col] == "Gender") {
      if (children[col].innerText == "Masculine") {
        const mascRadio = document.getElementById("radioMasc");
        mascRadio.checked = true;
      } else {
        const femRadio = document.getElementById("radioFem");
        femRadio.checked = true;
      }
    } else if (
      ["Education Level", "Recruitment Strategy"].includes(
        TABLE_ATTRIBUTE_ORDER[col]
      )
    ) {
      const options = Array.from(elemListOrder[col].options);
      const optionToSelect = options.find(
        (item) => item.text == children[col].innerText
      );
      optionToSelect.selected = true;
    } else if (elemListOrder[col]) {
      elemListOrder[col].value = children[col].innerText;
    }
  }
  const isToUpdate = document.getElementById("checkToUpdate");
  isToUpdate.checked = true;
};

// To remove candidate data from the database
const removeItem = async (elemID) => {
  const baseUrl = "http://127.0.0.1:5000/candidate/";

  const url = baseUrl.concat(elemID);
  if (confirm(`Confirmar remoção de item ${elemID}.`)) {
    await fetch(url, {
      method: "delete",
    });
    location.reload();
  }
};
