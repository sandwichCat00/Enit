// =====================
// Add Dynamic Fields
// =====================
function addSkill() {
    const container = document.getElementById('skills-container');
    const div = document.createElement('div');
    div.classList.add('skill-row');
    div.innerHTML = `
        <input type="text" name="skills_name[]" placeholder="Skill Name" required>
        <select name="skills_level[]" required>
            <option value="">Level</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
        </select>
    `;
    container.appendChild(div);
}

function addProject() {
    const container = document.getElementById('projects-container');
    const div = document.createElement('div');
    div.classList.add('project-row');
    div.innerHTML = `
        <input type="text" name="project_title[]" placeholder="Title" required>
        <input type="text" name="project_desc[]" placeholder="Description" required>
        <input type="text" name="project_tech[]" placeholder="Technologies (comma-separated)" required>
        <input type="url" name="project_link[]" placeholder="Link">
    `;
    container.appendChild(div);
}

function addIntern() {
    const container = document.getElementById('internships-container');
    const div = document.createElement('div');
    div.classList.add('intern-row');
    div.innerHTML = `
        <input type="text" name="intern_company[]" placeholder="Company">
        <input type="text" name="intern_role[]" placeholder="Role">
        <input type="number" name="intern_duration[]" placeholder="Duration (months)" min="0">
        <input type="number" name="intern_stipend[]" placeholder="Stipend (monthly)" min="0">
    `;
    container.appendChild(div);
}

function addAchievement() {
    const container = document.getElementById('achievements-container');
    const div = document.createElement('div');
    div.classList.add('ach-row');
    div.innerHTML = `
        <input type="text" name="ach_title[]" placeholder="Title">
        <input type="number" name="ach_year[]" placeholder="Year" min="1900" max="2099">
        <select name="ach_level[]">
            <option value="">Level</option>
            <option value="college">College</option>
            <option value="inter-college">Inter-college</option>
            <option value="state">State</option>
            <option value="national">National</option>
            <option value="international">International</option>
        </select>
    `;
    container.appendChild(div);
}
