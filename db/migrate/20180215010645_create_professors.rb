class CreateProfessors < ActiveRecord::Migration[5.1]
  def change
    create_table :professors do |t|
      t.string :email_id
      t.string :name
      t.string :website
      t.string :research

      t.timestamps
    end
  end
end
