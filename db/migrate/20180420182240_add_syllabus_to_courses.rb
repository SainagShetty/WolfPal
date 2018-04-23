class AddSyllabusToCourses < ActiveRecord::Migration[5.1]
  def change
    add_column :courses, :syllabus_file_id, :string
    add_column :courses, :syllabus_file_filename, :string
    add_column :courses, :syllabus_file_content_size, :string
    add_column :courses, :syllabus_file_content_type, :string
  end
end
